# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
from .jwplatform import JWPlatformIE


class BusinessInsiderIE(InfoExtractor):
    _VALID_URL = r'https?://(?:[^/]+\.)?asianfans\.(?:net)/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _TESTS = [{
        'url': 'http://player.asianfans.net/hydrax/player/?value=-KSYNd_c_&subon=/sub05hkfree.vtt',
        'only_matching': True,
    }, {
        'url': 'http://player.asianfans.net/hydrax/player/?value=Ikz_TVN2J&subon=/sub05hkfree.vtt',
        'only_matching': True,
    }]

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        video_id, display_id = mobj.groups()

        webpage = self._download_webpage(url, video_id)
        video_data = self._extract_jwplayer_data(webpage, video_id, require_title=False)
        return self.url_result(
            'jwplatform:%s' % jwplatform_id, ie=JWPlatformIE.ie_key(),
            video_id=video_id)
