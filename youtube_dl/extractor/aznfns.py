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
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        jwplatform_id = self._search_regex(
            (r'data-media-id=["\']([a-zA-Z0-9]{8})',
             r'id=["\']jwplayer_([a-zA-Z0-9]{8})',
             r'id["\']?\s*:\s*["\']?([a-zA-Z0-9]{8})'),
            webpage, 'jwplatform id')
        return self.url_result(
            'jwplatform:%s' % jwplatform_id, ie=JWPlatformIE.ie_key(),
            video_id=video_id)
