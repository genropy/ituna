# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tracks',legacy_name='main.tracks',legacy_db='chinook',pkey='trackid',caption_field='name',name_long='tracks',name_plural='tracks')
        tbl.column('trackid',dtype='I',name_long='Id',legacy_name='TrackId')
        tbl.column('name',size='0:200',name_long='Name',legacy_name='Name')
        tbl.column('albumid',dtype='I',name_long='Album',legacy_name='AlbumId',indexed=True,unique=False).relation('albums.albumid',
                                                                                                                    relation_name='tracks',
                                                                                                                    onDelete='raise', 
                                                                                                                    meta_thmode='dialog')
        tbl.column('mediatypeid',dtype='I',name_long='Media type',legacy_name='MediaTypeId',indexed=True,unique=False).relation('media_types.mediatypeid',
                                                                                                                        relation_name='tracks',
                                                                                                                         onDelete='raise', 
                                                                                                                        meta_thmode='dialog')
        tbl.column('genreid',dtype='I',name_long='Genre',legacy_name='GenreId',indexed=True,unique=False).relation('genres.genreid',
                                                                                                                    onDelete='raise', 
                                                                                                                    relation_name='tracks',
                                                                                                                    meta_thmode='dialog')
        tbl.column('composer',size='0:220',name_long='Composer',legacy_name='Composer')
        tbl.column('milliseconds',dtype='I',name_long='Milliseconds',legacy_name='Milliseconds')
        tbl.column('bytes',dtype='I',name_long='Bytes',legacy_name='Bytes')
        tbl.column('unitprice',dtype='N', name_long='Price',legacy_name='UnitPrice')
