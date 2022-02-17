# All Falcon 9 launches in 2022 #
## using Django ## 

**See app on https://djangofalcon9.herokuapp.com/**

Project includes:
 - user authentication (only registered users can edit or delete boosters,flights and missions)
 - usage of relations: 
   - ManyToOne (e.g. booster reused for different flights)
   - OneToOne (e.g. each flight is assigned to one unique mission)
- deployment of project to heroku
- usage of **Cloudinary** (cloud-based image and video management services) to enable usage of ImageFields when running on Heroku

### Models ###

There are 5 different models:
   - Mission
   - Booster
   - Launch site
   - Launch complex (connects to one launch site)
   - Flight (connects to one booster and one mission)