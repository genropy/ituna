#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('customerid')
        r.fieldcell('firstname')
        r.fieldcell('lastname')
        r.fieldcell('company')
        r.fieldcell('address')
        r.fieldcell('city')
        r.fieldcell('state')
        r.fieldcell('country')
        r.fieldcell('postalcode')
        r.fieldcell('phone')
        r.fieldcell('fax')
        r.fieldcell('email')
        r.fieldcell('supportrepid')

    def th_order(self):
        return 'customerid'

    def th_query(self):
        return dict(column='firstname', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('customerid')
        fb.field('firstname')
        fb.field('lastname')
        fb.field('company')
        fb.field('address')
        fb.field('city')
        fb.field('state')
        fb.field('country')
        fb.field('postalcode')
        fb.field('phone')
        fb.field('fax')
        fb.field('email')
        fb.field('supportrepid')
        center = bc.contentPane(region='center')
        center.dialogTableHandler(relation='@invoices')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
