# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('playlists',legacy_name='main.playlists',legacy_db='chinook',pkey='playlistid',caption_field='name',name_long='playlists',name_plural='playlists')
        tbl.column('playlistid',dtype='I',name_long='Id',legacy_name='PlaylistId')
        tbl.column('name',size='0:120',name_long='name',legacy_name='Name')
