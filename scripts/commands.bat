 כדי לראות את שם הCOLLECTION :
   def get_col_name(self):
        return self.db.list_collection_names()[0]



oc delete all --all
oc delete pvc --all
oc delete configmap --all
oc delete secret --all



docker build -t  danc12/image_open_mongo_21:v5 .

docker push danc12/image_open_mongo_21:v5


oc apply -f fastapi-deployment.yaml

oc apply -f fastapi-service.yaml

oc apply -f fastapi-route.yaml

oc get route