import json
import urllib, urllib2
import html2text
import codecs

def main():
    var = raw_input("Please enter query: ")
    res = run_query(var)
    for r in res:
        print 'title: ' + r['title'] + '\n'
        print 'link: ' + r['link'] + '\n'
        print 'summary: ' + r['summary'].encode('ascii', 'ignore') + '\n'



def run_query(search_terms):
    query = urllib.urlencode({'q': search_terms})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_response = urllib.urlopen(url)
    search_results = search_response.read()
    results = json.loads(search_results)


  
    # Create our results list which we'll populate.
    resultsForSearch = []
    h = html2text.HTML2Text()
    try:

        # Loop through each page returned, populating out results list.
        for result in results['responseData']['results']:
            
 
            resultsForSearch.append({
                'title': result['titleNoFormatting'],
                'link': result['url'],
                'summary': h.handle(result['content'])})

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError, e:
        print "Error when querying the google API: ", e

    # Return the list of results to the calling function.
    return resultsForSearch
    
    
if __name__ == "__main__":
    main()