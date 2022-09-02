import numpy as np
res ={'Zahraa Al Maadi': 99,'Mokattam': 60,'New Cairo - El Tagamoa': 65,'Shorouk City': 85,'Al Manial': 11,'Sheikh Zayed': 83,'6th of October': 2,'Madinaty': 49,'Hadayek 6th of October': 32,'Heliopolis': 38,'Asyut City': 16,'New Capital City': 66,'Smoha': 90,'10th of Ramadan': 0,'Nasr City': 64,'North Coast': 70,'Ras al-Bar': 73,'Glim': 30,'New Nozha': 69,'Hurghada': 41,'Kafr Abdo': 44,'Laurent': 46,'Miami': 57,'Obour City': 71,'Agami': 5,'Sidi Beshr': 88,'Katameya': 45,'Badr City': 17,'Sheraton': 84,'Faisal': 23,'Dokki': 21,'Rehab City': 74,'Stanley': 92,'Gianaclis': 28,'Ain Shams': 7,'Zezenia': 101,'Camp Caesar': 19,'Shubra al-Khaimah': 87,'West Somid': 97,'Saba Pasha': 76,'Hadayek al-Ahram': 34,'Victoria': 96,'Maadi': 47,'Hadayek al-Kobba': 35,'Nakheel': 63,'Mandara': 51,'Helmeyat El Zaytoun': 39,'Tanta': 94,'Sidi Gaber': 89,'Mansura': 52,'Zagazig': 98,'Asafra': 15,'Salam City': 77,'Sharm al-Sheikh': 80,'Roushdy': 75,'Al Ibrahimiyyah': 10,'Giza District': 29,'Maamoura': 48,'Haram': 37,'Fleming': 25,'Mohandessin': 58,'Ismailia City': 43,'Moharam Bik': 59,'Agouza': 6,'Al Hadrah': 9,'Seyouf': 79,'New Heliopolis': 68,'Shebin al-Koum': 82,'Gesr Al Suez': 27,'Hadayek Helwan': 33,'Downtown Cairo': 22,'Zohour District': 102,'Imbaba': 42,'Suez District': 93,'Shubra': 86,'Marg': 53,'Matareya': 56,'Dar al-Salaam': 20,'Maryotaya': 55,'Sporting': 91,'Gouna': 31,'Sharq District': 81,'Helwan': 40,'Abu Qir': 3,'Marsa Matrouh': 54,'Almazah': 13,'Gamasa': 26,'Mahalla al-Kobra': 50,'15 May City': 1,'Zamalek': 100,'Alamein': 12,'Montazah': 62,'San Stefano': 78,'Tersa': 95,'Moneeb': 61,'Borg al-Arab': 18,'Ain Sukhna': 8,'New Damietta': 67,'Fayed': 24,'Abu Talat': 4,'Ras Sedr': 72,'Amreya': 14,'Hammam': 36}

def Location_City(City):
    if City in res:
        return [res[City]]
    else :
        return 'The City Not Found'

def Property_Type(Type) :
    if Type == 'Apartment' : 
        return [0]
    elif Type == 'Duplex' :
        return [2]
    elif Type == 'Stand Alone Villa' :
        return [3]
    elif Type == 'Twin House' :
        return [5]
    elif Type == 'Town House' :
        return [4]
    elif Type == 'Chalet' :
        return [1]
    
    
def Furnished_st(x) :
    if x == 'Yes' : 
        return [1]
    elif x == 'No' :
        return [0]

def preprocess_data(data) :
    City = Location_City(data['Location_City'])[0]
    
    Beds = data['Bed_Rooms']
    
    Baths = data['Bath_Rooms']
    
    Space = data['Home_Space_SQM']   
    
    Furnished = Furnished_st(data['Furnished'])[0]
    
    Property = Property_Type(data['Property_Type'])[0]
    
    
    final_data = [City, Beds, Baths, Space, Furnished ,Property]
    
    return np.array(final_data)