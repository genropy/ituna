# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('genres',legacy_name='main.genres',legacy_db='chinook',pkey='genreid',caption_field='name',name_long='genres',name_plural='genres')
        tbl.column('genreid',dtype='I',name_long='Id',legacy_name='GenreId')
        tbl.column('name',size='0:120',name_long='Name',legacy_name='Name')
        tbl.formulaColumn('tot_genre', select=dict(columns='SUM($totprice)', table='ituna.invoice_items', where='@trackid.genreid = #THIS.genreid') , name_long='Tot genre')