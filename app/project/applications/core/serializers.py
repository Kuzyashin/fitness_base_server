from rest_framework import serializers


class SamplePayloadSerializer(serializers.Serializer):
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    job = serializers.CharField()
    dateOfBirth = serializers.DateTimeField()
    country = serializers.CharField()

    @classmethod
    def generate(cls):
        return cls(data=[
            {
                "firstName": "Jack",
                "lastName": "Griffith",
                "job": "Nunc Ac Mattis Inc.",
                "dateOfBirth": "1984-10-20T20:22:56+06:00",
                "country": "Greenland"
            },
            {
                "firstName": "Leo",
                "lastName": "Jayme",
                "job": "Velit Company",
                "dateOfBirth": "1960-08-15T18:07:11+06:00",
                "country": "Bahrain"
            },
            {
                "firstName": "Hayley",
                "lastName": "Lynn",
                "job": "Cras Sed Corp.",
                "dateOfBirth": "1969-07-30T13:22:10+06:00",
                "country": "Niger"
            },
            {
                "firstName": "Knox",
                "lastName": "Anne",
                "job": "Et Commodo At Corp.",
                "dateOfBirth": "1985-02-10T01:52:38+06:00",
                "country": "Equatorial Guinea"
            },
            {
                "firstName": "Edan",
                "lastName": "Trevor",
                "job": "Fringilla Cursus Inc.",
                "dateOfBirth": "1966-09-21T13:14:39+06:00",
                "country": "Saint Pierre and Miquelon"
            },
        ], many=True)

