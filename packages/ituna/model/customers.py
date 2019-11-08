# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('customers',legacy_name='main.customers',
                            legacy_db='chinook',
                            pkey='customerid',
                            caption_field='full_name',
                            name_long='Customer',name_plural='Customers')
        tbl.column('customerid',dtype='I',name_long='Id',legacy_name='CustomerId')
        tbl.column('firstname',size='0:40',name_long='Firstname',legacy_name='FirstName')
        tbl.column('lastname',size='0:20',name_long='Lastname',legacy_name='LastName')
        tbl.column('company',size='0:80',name_long='Company',legacy_name='Company')
        tbl.column('address',size='0:70',name_long='Address',legacy_name='Address')
        tbl.column('city',size='0:40',name_long='City',legacy_name='City')
        tbl.column('state',size='0:40',name_long='State',legacy_name='State')
        tbl.column('country',size='0:40',name_long='Country',legacy_name='Country')
        tbl.column('postalcode',size='0:10',name_long='Postalcode',legacy_name='PostalCode')
        tbl.column('phone',size='0:24',name_long='Phone',legacy_name='Phone')
        tbl.column('fax',size='0:24',name_long='Fax',legacy_name='Fax')
        tbl.column('email',size='0:60',name_long='Email',legacy_name='Email')
        tbl.column('supportrepid',dtype='I',name_long='Support Rep',legacy_name='SupportRepId',indexed=True,unique=False).relation('employees.employeeid',
                                                                                                                                    relation_name='customers',
                                                                                                                                    onDelete='raise', 
                                                                                                                                    meta_thmode='dialog')
        tbl.formulaColumn('full_name', "$firstname ||' '||$lastname", name_long='Full name')