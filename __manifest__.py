{
    'name':'HMS',
    'summary':'Hospital Module',
    'version':'1.0.0',
    'depends':['mail','account'],
    'data':[
        'security/ir.model.access.csv',
        # 'security/security.xml',
        'data/sequence.xml',
        'views/patient.xml',
         'views/sector.xml',
         'views/dictor.xml',
         'views/appointment.xml',
          'views/prescription.xml',
          'views/account.xml'
    ],
    'installable':True,
    'application':True,
    'sequence':-100,
    'asset':'static/description/icon.png'
}