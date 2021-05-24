{
    'name' : 'ABC Hosptal',
    'version' : '1.0',
    'summary': 'Hosptal Management',
    'sequence' : 4,
    'description' : 'ABC Hosptal description.',
    'depends' : ['base'],
    'data' : [
        'security/hospital_security.xml',
        'security/ir.model.access.csv',

        'views/management_views.xml',
        'views/doctors_views.xml',
        'views/patient_views.xml',
        'views/medicine_views.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}