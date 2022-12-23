# This entity is used to get a dataset from the Data Fair API.

import requests as req


class Dataset:

    URL_BASE = "https://koumoul.com/data-fair/api/v1/datasets/dpe-france/"
    url = ""

    def __init__(self,
                 fields="nom_methode_dpe",
                 size=0,
                 select=(),
                 sort=(),
                 geo_distance={"longitude": 0, "latitude": 0, "distance": 0}):
        self.fields = fields

        if (size > 10000):
            return "The data size is too big"
        else:
            self.size = size
        self.select = select
        self.sort = sort
        self.url = self.URL_BASE + "lines"
        self.geo_distance = geo_distance
        if (self.size != 0):
            self.url = self.url+"?size="+str(self.size)
        if (len(self.select) != 0):
            if (type(self.select) == str):
                self.url = self.url+"&select="+self.select
            else:
                self.url += "&select=" + "%2C".join(self.select)
        if (len(self.sort) != 0):
            self.url += "&sort=" + "%2C".join(self.sort)
        if (self.geo_distance["longitude"] != 0 and self.geo_distance["latitude"] != 0 and self.geo_distance["distance"] != 0):
            self.url += "&geo_distance=" + \
                str(self.geo_distance["longitude"]) + \
                "%2C"+str(self.geo_distance["latitude"]) + \
                "%2C"+str(self.geo_distance["distance"])

    @classmethod
    def get_fields(cls):
        """
        Returns a list of fields for which value is desired
        List of fields :
            nom_methode_dpe
            version_methode_dpe
            date_etablissement_dpe
            consommation_energie
            classe_consommation_energie
            estimation_ges
            classe_estimation_ges
            annee_construction
            surface_thermique_lot
            latitude
            longitude
            tr001_modele_dpe_type_libelle
            tr002_type_batiment_description
            code_insee_commune_actualise
            tv016_departement_code
            geo_adresse
            geo_score
        """
        return cls.fields

    @classmethod
    def getSize(cls):
        """
        Return size of the dataset
        """
        return cls.size

    @classmethod
    def getSelect(cls):
        """
        Return the selected filed for the dataset
        """
        return cls.select

    @classmethod
    def getSort(cls):
        """
        Return the sort filed sot this dataset
        """
        return cls.sort

    def getFieldValue(self):
        """
        Return list of value of the field selected
        dependents on the size of the dataset
        Args : 
            fields : field name
            size   : int
        Return:
            json data
        """
        resp = req.get(self.URL_BASE + "values/" + self.fields +
                       "?size=" + str(self.size))
        return resp.json()

    def get_data(self):
        """
        Return list of data of the dataset
        dependents on the size of the dataset and the field selected
        Args :
            select : tupple of field name
            sort   : tupple of field name
            size   : int
        Return:
            json data
        """
        try:
            resp = req.get(self.url)
            return resp.json()
        except:
            return "An error occured with the API please check your parameters\n"+self.url

    def dumpURL(self):
        """
        Return the url of the dataset
        """
        return self.url

