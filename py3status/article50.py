import urllib.request, json

class Py3status:

	def article50(self):
	    with urllib.request.urlopen("https://petition.parliament.uk/petitions/241584/count.json") as url:
        	data = json.loads(url.read().decode())
	        return { 'full_text': 'Article 50: ' + str(data['signature_count']),
			 'cached_until': 60
		}
