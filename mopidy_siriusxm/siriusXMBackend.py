from __future__ import absolute_import, unicode_literals

import logging
import threading
import pykka

import siriusxm

from mopidy import backend, httpclient

from mopidy_siriusxm import Extension

logger = logging.getLogger(__name__)


class SiriusXM(pykka.ThreadingActor, backend.Backend):

    _logged_in = threading.Event()
    _logged_out = threading.Event()
    _logged_out.set()

    def __init__(self, config, audio):
        super(SiriusXM, self).__init__()

        self._config = config
        self._audio = audio
        self._actor_proxy = None
        self._session = None
        self._event_loop = None
        self._bitrate = None

        # self.library = library.SiriusXMLibraryProvider(backend=self)
        # self.playback = playback.SiriusXMPlaybackProvider(audio=audio, backend=self)
        self.uri_schemes = ['siriusxm']

    def on_start(self):
        self._actor_proxy = self.actor_ref.proxy()
        # self._session = self._get_session(self._config)

        # self._event_loop = siriusXM.EventLoop(self._session)
        # self._event_loop.start()

        username = self._config['siriusxm']['username']
        password = self._config['siriusxm']['password']
        remember_me = self._config['siriusxm']['remember_me']

        authenticate = siriusxm.auth(self._config)
        authenticate.login(username, password, remember_me)

    def on_stop(self):
        logger.debug('Logging out of Sirius XM')
        # self._session.logout()
        self._logged_out.wait()
        # self._event_loop.stop()

    # def _get_session(self, config):
    #    session = siriusXM.Session(self._get_siriusXM_config(config))

    #    session.connection.allow_network = config['siriusxm']['allow_network']

    #    backend_actor_proxy = self._actor_proxy

    #    session.on(siriusXM.SessionEvent.CONNECTION_STATE_UPDATED, on_connection_state_changed, self._logged_in, self._logged_out, backend_actor_proxy)
    #    session.on(siriusXM.SessionEvent.PLAY_TOKEN_LOST, on_play_token_lost, backend_actor_proxy)

    #    return session

    def _get_siriusXM_config(self, config):
        ext = Extension()
        siriusXM_config = siriusxm.config()

        if config['siriusxm']['allow_cache']:
            siriusXM_config.cache_location = ext.get_cache_dir(config)
        else:
            siriusXM_config.cache_location = None

        siriusXM_config.settings_location = ext.get_data_dir(config)

        proxy_uri = httpclient.format_proxy(config['siriusxm']['proxy'], auth=False)

        if proxy_uri is not None:
            logger.debug('Connecting to Sirius XM through proxy: %s', proxy_uri)

        siriusXM_config.proxy = proxy_uri
        siriusXM_config.proxy_username = config['siriusxm']['proxy_username']
        siriusXM_config.proxy_password = config['siriusxm']['proxy_password']

        return siriusXM_config

    def on_logged_in(self):
        pass
        # self._session.playlist_container.on(spotify.PlaylistContainerEvent.CONTAINER_LOADED, playlists.on_container_loaded)
        # self._session.playlist_container.on(spotify.PlaylistContainerEvent.PLAYLIST_ADDED, playlists.on_playlist_added)
        # self._session.playlist_container.on(spotify.PlaylistContainerEvent.PLAYLIST_REMOVED, playlists.on_playlist_removed)
        # self._session.playlist_container.on(spotify.PlaylistContainerEvent.PLAYLIST_MOVED, playlists.on_playlist_moved)

        # def on_play_token_lost(self):
        #    if self._session.player.state == siriusXM.PlayerState.PLAYING:
        #        self.playback.pause()
        #        logger.warning('Sirius XM has been paused because your account is being used somewhere else.')

    # def on_connection_state_changed(session, logged_in_event, logged_out_event, backend):
    # Called from the pysiriusxm event loop, and not in an actor context.
    #    if session.connection.state is siriusXM.ConnectionState.LOGGED_OUT:
    #        logger.debug('Logged out of Sirius XM')
    #        logged_in_event.clear()
    #        logged_out_event.set()
    #    elif session.connection.state is siriusXM.ConnectionState.LOGGED_IN:
    #        logger.info('Logged in to Sirius XM in online mode')
    #        logged_in_event.set()
    #        logged_out_event.clear()
    #        backend.on_logged_in()
    #    elif session.connection.state is siriusXM.ConnectionState.DISCONNECTED:
    #        logger.info('Disconnected from Sirius XM')
    #    elif session.connection.state is siriusXM.ConnectionState.OFFLINE:
    #        logger.info('Logged in to Sirius XM in offline mode')
    #        logged_in_event.set()
    #        logged_out_event.clear()

    # def on_play_token_lost(session, backend):
    # Called from the pysiriusxm event loop, and not in an actor context.

# logger.debug('Sirius XM play token lost')
#    backend.on_play_token_lost()
