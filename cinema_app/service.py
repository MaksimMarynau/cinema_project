def get_client_ip(request):
    x_forwardef_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwardef_for:
        ip = x_forwardef_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
