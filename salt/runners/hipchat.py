import urllib
import urllib2
import ssl

def show(jid, arg, function, stamp, tgt, tgt_type, user, url, auth_token, room_id, bot_name):
    result = brief_format(jid, arg, function, stamp, tgt, tgt_type, user)
    values = {'auth_token': auth_token,
          'room_id': room_id,
          'from': bot_name,
          'message': result}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    sslcontext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sslcontext.set_default_verify_paths()
    response = urllib2.urlopen(req, context=sslcontext)

def brief_format(jid, arg, function, stamp, tgt, tgt_type, user):
    return "[" + str(jid) + "] salt '" + str(tgt) + "' " + str(function) + " " + str(arg)
