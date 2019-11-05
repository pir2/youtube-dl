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

        iframe_url = self._search_regex(
            r'<iframe[^>]+src="([^"]+)"', webpage, 'iframe URL')

        ifs_page = self._download_webpage(iframe_url, video_id)
        jwplayer_data = self._find_jwplayer_data(
            ifs_page, video_id, transform_source=js_to_json)
        info_dict = self._parse_jwplayer_data(
            jwplayer_data, video_id, require_title=False, base_url=iframe_url)

        info_dict.update({
            'id': video_id,
            'title': 'default',
            'description': 'default',
            'series': 'default'
        })
