from rest_framework import serializers


class DataCenterSetupSerializer(serializers.Serializer):
    """
    Serializer for DataCenterSetups.
    It defines how many DM (DevOps Managers) and DEs (DevOps Engineers)
    are available to handle a range of DataCenters.
    """
    DM_capacity = serializers.IntegerField()
    DE_capacity = serializers.IntegerField()
    data_centers = serializers.JSONField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_de = None

    def get_minimum_de(self):
        """Retrieves the minimum amount of DEs necessary to handle the range of Data Centers"""
        if self.min_de:
            # This makes sure that the value won't be calculated a second time
            return self.min_de

        total_servers = sum([dc["servers"] for dc in self.validated_data["data_centers"]])
        min_de = (total_servers - self.validated_data["DM_capacity"]) / self.validated_data["DE_capacity"]
        self.min_de = round(min_de)
        
        return self.min_de

    def get_best_datacenter(self):
        """Calculates which is the best DataCenter for the DMs to be"""
        min_or_max = None
        
        if self.validated_data["DM_capacity"] > self.get_minimum_de():
            min_or_max = min
        else:
            min_or_max = max
        
        return min_or_max(self.validated_data["data_centers"], key=lambda k: k["servers"])["name"]

    def get_return_data(self):
        """The expected output"""
        return {"DE": self.get_minimum_de(), "DM_data_center": self.get_best_datacenter()}
