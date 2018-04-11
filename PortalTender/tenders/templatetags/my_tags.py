from django import template

register = template.Library()

@register.simple_tag
def get_code(tender_data):
    return tender_data['code']

@register.simple_tag
def get_subject(tender_data):
    return tender_data['subject']

@register.simple_tag
def get_customer(tender_data):
    return tender_data['customer']

@register.simple_tag
def get_price(tender_data):
    return tender_data['price']

@register.simple_tag
def get_deadline(tender_data):
    return tender_data['deadline']

@register.simple_tag
def get_link(tender_data):
    return tender_data['link']