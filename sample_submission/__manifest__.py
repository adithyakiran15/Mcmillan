{
    'name': 'sample submission',
    'author': 'macmillanglobal',
    'version': '1.0',
    'summary': 'development',
    'depends': [ 'base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/homepage.xml',
        'report/sample_report.xml',
        'report/sample_report_temp.xml',


            ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
