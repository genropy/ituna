# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('playlist_track',legacy_name='main.playlist_track',
                        legacy_db='chinook',pkey='_multikey',
                        caption_field='_multikey',
                        name_long='Playlist track',
                        name_plural='Playlist tracks')
        tbl.column('playlistid',dtype='I',name_long='Playlist',legacy_name='PlaylistId').relation('playlists.playlistid',
                                                                                                    relation_name='tracks',
                                                                                                    onDelete='raise',
                                                                                                    meta_thmode='dialog')
        tbl.column('trackid',dtype='I',name_long='Track',legacy_name='TrackId',indexed=True,unique=False).relation('tracks.trackid',
                                                                                                    onDelete='raise',
                                                                                                    relation_name='playlists',
                                                                                                    meta_thmode='dialog')
        tbl.column('_multikey',name_long='_multikey')
