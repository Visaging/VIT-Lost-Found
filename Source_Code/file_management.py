import firebase_admin as fa
from firebase_admin import credentials, firestore
from google.cloud.firestore import FieldFilter

if not fa._apps:
    cred=credentials.Certificate("serviceAccountKey.json")
    fa.initialize_app(cred)
db=firestore.client()

def loadusers():
    users=db.collection('users')
    docs=users.stream()

    userslist=[]
    for i in docs:
        userslist.append(i.to_dict())
    return userslist

def saveuser(userslist):
    if not userslist:
        return
    newuser=userslist[-1]
    exists=db.collection('users').where(filter=FieldFilter('regno', '==', newuser['regno'])).get()
    if not exists:
        db.collection('users').add(newuser)

def loaditems():
    items=db.collection('items')
    docs=items.stream()

    itemslist=[]
    for i in docs:
        itemslist.append(i.to_dict())
    return itemslist

def saveitem(itemslist):
    if not itemslist:
        return
    for i in itemslist:
        docs=db.collection('items').where(filter=FieldFilter('id', '==', i['id'])).get()
        if docs:
            docid=docs[0].id
            db.collection('items').document(docid).set(i)
        else:
            db.collection('items').add(i)
