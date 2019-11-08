# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('albums',legacy_name='main.albums',legacy_db='chinook',pkey='albumid',caption_field='title',name_long='Album',name_plural='Albums')
        tbl.column('albumid',dtype='I',name_long='Id',legacy_name='AlbumId')
        tbl.column('title',size='0:160',name_long='Title',legacy_name='Title')
        tbl.column('artistid',dtype='I',name_long='Artist',legacy_name='ArtistId',indexed=True,unique=False).relation('artists.artistid',
                                                                                                                        onDelete='raise',
                                                                                                                        relation_name='albums',
                                                                                                                        meta_thmode='dialog')
