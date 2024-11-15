import whois

def get_updated_date(url):
    domain = whois.whois(url)
    print(domain)

get_updated_date("http://currentwellnessraleigh.com/")
