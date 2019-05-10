import json
from time import sleep
import requests

def retrieve_comment_json(article):
    '''
    Given a New York Times article link, grabs all comments and places their json data in a list
    '''
    article=article.replace(':','%253A') #convert the : to an HTML entity
    article=article.replace('/','%252F') #convert the / to an HTML entity
    offset=0 #Start off at the very beginning
    total_comments=1 #set a fake minimum number of contents
    comment_list=[] #Set up a place to store the results
    while total_comments>offset:
        url='http://www.nytimes.com/svc/community/V3/requestHandler?callback=NYTD.commentsInstance.drawComments&method=get&cmd=GetCommentsAll&url='+article+'&offset='+str(offset)+'&sort=newest' #store the secret URL
        sleep(.5) #They don't like you to vist the page too quickly so take a half a second break before downloading
        file = requests.get(url).text
        file=file.replace('/**/ NYTD.commentsInstance.drawComments(','') #remove some clutter
        file=file[:-2] #remove some clutter
        results=json.loads(file) #load the file as json
        comment_list=comment_list+results['results']['comments']
        if offset==0: #print out the number of comments, but only the first time through the loop
            total_comments=results['results']['totalCommentsFound'] # store the total number of comments
            print('Found '+str(total_comments)+' comments')

        offset=offset+25 #increment the counter
        
    return comment_list #return the list back

def comment_body_list(comment_list):
    '''
    Given a list of JSON comments, returns a list of the text from each comment
    '''
    comments = []
    for comment in comment_list: #loop through the list
        comments.append(comment['commentBody'])
    return comments 


'''
Fields that you can retrieve from each comment:
commentID
status
commentSequence
userID
userDisplayName
userLocation
userTitle
userURL
picURL
commentTitle
commentBody
createDate
updateDate
approveDate
recommendations
replyCount
replies
editorsSelection
parentID
parentUserDisplayName
depth
commentType
trusted
recommendedFlag
permID
isAnonymous
'''

    
