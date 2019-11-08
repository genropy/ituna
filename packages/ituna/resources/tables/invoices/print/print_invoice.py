from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Print Invoice'

class Main(BaseResourcePrint):
    batch_title = 'Print invoice'
    html_res = 'html_res/invoice'
    templates = 'ituna_base'
