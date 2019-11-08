# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('invoices',legacy_name='main.invoices',legacy_db='chinook',pkey='invoiceid',caption_field='invoiceid',name_long='Invoice',name_plural='Invoices')
        tbl.column('invoiceid',dtype='I',name_long='Id',legacy_name='InvoiceId')
        tbl.column('customerid',dtype='I',name_long='Customer',legacy_name='CustomerId',indexed=True,unique=False).relation('customers.customerid',
                                                                                                                            relation_name='invoices',
                                                                                                                            onDelete='raise', 
                                                                                                                            meta_thmode='dialog')
        tbl.column('invoicedate',dtype='D',name_long='Date',legacy_name='InvoiceDate')
        tbl.column('billingaddress',size='0:70',name_long='Bill address',legacy_name='BillingAddress')
        tbl.column('billingcity',size='0:40',name_long='Billcity',legacy_name='BillingCity')
        tbl.column('billingstate',size='0:40',name_long='Bill state',legacy_name='BillingState')
        tbl.column('billingcountry',size='0:40',name_long='Bill country',legacy_name='BillingCountry')
        tbl.column('billingpostalcode',size='0:10',name_long='Bill postcode',legacy_name='BillingPostalCode')
        tbl.column('total',dtype='N',name_long='Total',legacy_name='Total')
