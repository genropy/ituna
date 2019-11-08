# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('employees',legacy_name='main.employees',legacy_db='chinook',pkey='employeeid',caption_field='lastname',name_long='Employee',name_plural='Employees')
        tbl.column('employeeid',dtype='I',name_long='Id',legacy_name='EmployeeId')
        tbl.column('lastname',size='0:20',name_long='Last name',legacy_name='LastName')
        tbl.column('firstname',size='0:20',name_long='First name',legacy_name='FirstName')
        tbl.column('title',size='0:30',name_long='Title',legacy_name='Title')
        tbl.column('reportsto',dtype='I',name_long='Reports to',legacy_name='ReportsTo',indexed=True,unique=False).relation('employees.employeeid',
                                                                                                                            relation_name='subordinates',
                                                                                                                            onDelete='raise', 
                                                                                                                            meta_thmode='dialog')
        tbl.column('birthdate',dtype='D',name_long='Birthdate',legacy_name='BirthDate')
        tbl.column('hiredate',dtype='D',name_long='Hiredate',legacy_name='HireDate')
        tbl.column('address',size='0:70',name_long='Address',legacy_name='Address')
        tbl.column('city',size='0:40',name_long='City',legacy_name='City')
        tbl.column('state',size='0:40',name_long='State',legacy_name='State')
        tbl.column('country',size='0:40',name_long='Country',legacy_name='Country')
        tbl.column('postalcode',size='0:10',name_long='Postalcode',legacy_name='PostalCode')
        tbl.column('phone',size='0:24',name_long='Phone',legacy_name='Phone')
        tbl.column('fax',size='0:24',name_long='Fax',legacy_name='Fax')
        tbl.column('email',size='0:60',name_long='Email',legacy_name='Email')
