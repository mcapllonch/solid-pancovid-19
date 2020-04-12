import pandas as pd
import os
import numpy as np
from datetime import datetime

class dummyDataHandler():
	def __init__(self):
		src_fldr = os.path.join('..','src')
		df = pd.read_csv(os.path.join(src_fldr, 'metadata.csv'))
		df = df.dropna(subset=['sha']).set_index('sha')
		self.data = df
		self.data.publish_time = self.data.publish_time.apply(clean_time)
		self.data.publish_time = self.data.publish_time.apply(lambda x: x.strftime('%Y-%m') if not pd.isna(x) else np.nan)
		self.dummy_keywords = ['mortality rate', 'extracorporeal membrane oxygenation (ECMO)', 'vaccine', 'interventions', 'clinical outcome', np.nan]
		self.setUp()

	def setUp(self):
		self.data['tag'] = [self.dummy_keywords[np.random.choice(np.arange(0,6), p=[0.02, 0.02, 0.02, 0.02,0.02, 0.9])] for i in range(self.data.shape[0])]
		self.data['phase'] = [f'Phase {np.random.choice(np.arange(1,6), p=[0.5, 0.3, 0.1, 0.075, 0.025])}' for i in range(self.data.shape[0])]

	def get_pivot(self):
		pv = pd.pivot_table(self.data.reset_index(), values=['sha'], index=['tag', 'phase', 'publish_time'], aggfunc=np.count_nonzero).reset_index().rename(columns={'sha':'count'})
		return pv


def clean_time(val):
    try:
        return datetime.strptime(val, '%Y-%m-%d')
    except:
        try:
            return datetime.strptime(val, '%Y %b %d')
        except:
            try:
                return datetime.strptime(val, '%Y %b')
            except:
                try:
                    return datetime.strptime(val, '%Y')
                except:
                    try:
                        return datetime.strptime('-'.join(val.split(' ')[:3]), '%Y-%b-%d')
                    except Exception as e:
                        return None