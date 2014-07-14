from api import NeoClient
from exceptions import (
    ActivityNotFound,
    AccountTooYoung,
)
import urls
# import re

class Activity(NeoClient):
    def get_monthly_freebie(self):
        """Monthly freebie for all pets."""
        response = self._player.get(urls.urls['monthly_freebie'])
        if 'Freebies For You!' not in response.text:
            raise ActivityNotFound("Monthly Freebie")
        if 'your account must be at least 30 days old' in response.text:
            raise AccountTooYoung(30)

    def get_omelette(self):
        """Tyrannian omelette"""
        query = {'type': 'get_omelette'}
        omelettePage = self._player.post(urls.urls['omelette'],
                                         data=query).text
        # Do logging
        # omelettePage.decode('utf-8').encode('ascii', 'ignore')
        if "Sabre-X" in omelettePage:
            return {'success': False, 'result': None, 'info': "Already taken."}
            print('Aready taken')
        if "Gone!!!" in  omelettePage:
            return {'success': False, 'result': None, 'info': "Omelette ran out."}
        #if(re.findall('items/([\d\w, _]+)\.gif\' width=80', omelettePage)):
        #    print(re.findall('items/([\d\w, _]+)\.gif\' width=80', omelettePage))
        #     return re.findall('items/([\d\w, _]+)\.gif\' width=80',
        #             omelettePage)[0]
        #    return {'success': False, 'result': something}
        #return omelettePage


