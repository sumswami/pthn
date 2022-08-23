from copy import deepcopy
import pandas


def cross_join(left, right):
    new_rows = [] if right else left
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows


def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem


def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(
                    value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for item in data:
                [rows.append(elem) for elem in flatten_list(
                    flatten_json(item, prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows

    return pandas.DataFrame(flatten_json(data_in))


if __name__ == '__main__':
    json_data = [
        {
            "status": "200",
            "message": "Successfully Retrieved from CACHE",
            "resultType": "contentDetails",
            "resultBody": {
                "title": "Landline home phone",
                "contentType": "content_topicinfo",
                "publishedId": "KM1083090",
                "version": "23.0",
                "id": "GJSabp4Ovv8fd6wZ7BmMa5",
                "status": "PUBLISHED",
                "contentTypeProperties": {
                    "topoption1ctaurlinnewwindow": "false",
                    "wfoffersignin": "false",
                    "additionalopiton1ctaurlnewwindow": "false",
                    "topicinfovideoid": "2800020,1500006,2800020",
                    "featured": "false",
                    "additionalopiton3ctaurlnewwindow": "false",
                    "shortdescription": "Learn about home phone plans, features, and more. Find out how to contact us.",
                    "additionalopiton2ctaurlnewwindow": "false",
                    "wfautostart": "false",
                    "wfunauthbreadcrumbs": "false",
                    "wfreqauthentication": "false",
                    "wfauthbreadcrumbs": "false",
                    "cfurlnewwindow": "false"
                },
                "tagSets": [
                    {
                        "fieldName": "topic",
                        "systemTagName": "topic",
                        "displayTagName": "Topic",
                        "tags": [
                            {
                                "systemTagName": "topic_landline",
                                "displayTagName": "Landline home phone"
                            }
                        ]
                    }
                ],
                "publishedDate": "2021-11-12T17:27:20.304+00:00",
                "lastModifiedDate": "2021-11-12T17:27:20.294+00:00",
                "seoNoIndex": "false",
                "excludeInternalSearch": "false",
                "excludeSpanish": "false"
            },
            "itemCreationTime": "1652327860317086"
        },
        {
            "status": "200",
            "message": "Successfully Retrieved from KMS",
            "resultType": "contentDetails",
            "resultBody": {
                "title": "Home phone - Billing & account",
                "contentType": "content_topicinfo",
                "publishedId": "KM1083095",
                "version": "10.0",
                "id": "0i6nTao1cE6oaKzod3rQ48",
                "status": "PUBLISHED",
                "contentTypeProperties": {
                    "featured": "false",
                    "shortdescription": "Get help managing your AT&T home phone service and account. ",
                    "iconimagepath": "/ecms/dam/att/consumer/help/image/icn-category-gray-60x45-myATT.png",
                    "additionalopiton1ctaurlnewwindow": "false",
                    "additionalopiton2ctaurlnewwindow": "false",
                    "additionalopiton3ctaurlnewwindow": "false",
                    "topoption1ctaurlinnewwindow": "false"
                },
                "topSolutionsList": [
                    {
                        "value": "{ \"contentId\" : \"iroQScclIwAWs61EEqkKF9\", \"contentType\" : \"content_instruct\", \"publishedId\" : \"KM1008625\", \"title\" : \"View bills online\" }"
                    },
                    {
                        "value": "{ \"contentId\" : \"RQDSXusRnp5CYKKh1KFkxA\", \"contentType\" : \"content_instruct\", \"publishedId\" : \"KM1061375\", \"title\" : \"Question AT&T bill charges\" }"
                    },
                    {
                        "value": "{ \"contentId\" : \"bsMVUYnted5NquUQXCjJf5\", \"contentType\" : \"content_instruct\", \"publishedId\" : \"KM1009608\", \"title\" : \"Add, change, or delete a stored payment method\" }"
                    },
                    {
                        "value": "{ \"contentId\" : \"XYl0uLxiW98b2y38FEG5L8\", \"contentType\" : \"content_parentinstruct\", \"publishedId\" : \"KM1045101\", \"title\" : \"Change home phone or long distance plan and services\" }"
                    },
                    {
                        "value": "{ \"contentId\" : \"p1idR7l48yArdbbBbUaVi5\", \"contentType\" : \"content_instruct\", \"publishedId\" : \"KM1061397\", \"title\" : \"View AT&T bill credits or adjustments\" }"
                    }
                ],
                "publishedDate": "2019-02-05T18:17:26.837+00:00",
                "lastModifiedDate": "2019-02-05T18:17:26.825+00:00",
                "seoNoIndex": "false",
                "excludeInternalSearch": "false",
                "excludeSpanish": "false"
            }
        },
        {
            "status": "200",
            "message": "Successfully Retrieved from KMS",
            "resultType": "contentDetails",
            "resultBody": {
                "title": "Home phone - Billing & account - Account & profile - Contact information",
                "contentType": "content_topicinfo",
                "publishedId": "KM1083164",
                "version": "4.0",
                "id": "ANrBTlVtjl9PJ6JNcB7Ey8",
                "status": "PUBLISHED",
                "contentTypeProperties": {
                    "featured": "false",
                    "shortdescription": "Learn how to update your contact information.",
                    "additionalopiton1ctaurlnewwindow": "false",
                    "additionalopiton2ctaurlnewwindow": "false",
                    "additionalopiton3ctaurlnewwindow": "false",
                    "topoption1ctaurlinnewwindow": "false"
                },
                "publishedDate": "2018-02-07T18:47:04.70+00:00",
                "lastModifiedDate": "2018-02-07T18:47:04.60+00:00",
                "seoNoIndex": "false",
                "excludeInternalSearch": "false",
                "excludeSpanish": "false"
            }
        }
    ]
    df = json_to_dataframe(json_data)
    print(df)
    df.to_csv('data.csv', mode='w')
