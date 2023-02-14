# cs344-microservice
## How to request data
The microservice accepts HTTP POST requests to the `/totalTime` endpoint. Running the service locally, the URL will be `http://localhost:5000/totalTime`

The body of the reqest must be JSON in the following basic structure:
```
{
  "intersections": [
    {
      "ramps": [
        {
          "style": "PERPENDICULAR",
          "inspectionType": "FULL"
        }
      ]
    }
  ]
}
```

The `intersections` field must be an array.

Each object in the `intersections` array must include a `ramps` field, which is an array.

Each object in the `ramps` field must include `style` and `inspectionType` fields, which are strings.

The following strings are accepted for the `style` field and are case-insensitive:
- COMBINATION
- PERPENDICULAR
- PARALLEL
- UNIQUE
- CUT_THROUGH

The following strings are accepted for the `inspectionType` field and are case-insensitive:
- FULL
- GO_BACK

### Example call
```
// using JS fetch API
const data = {
   "intersections": [
     {
       "ramps": [
         {
           "style": "PERPENDICULAR",
           "inspectionType": "FULL"
         },
         {
           "style": "UNIQUE",
           "inspectionType": "FULL"
         }
       ]
     },
     {
       "ramps": [
         {
           "style": "PARALLEL",
           "inspectionType": "FULL"
         },
         {
           "style": "COMBINATION",
           "inspectionType": "FULL"
         }
       ]
     },
     {
       "ramps": [
         {
           "style": "PARALLEL",
           "inspectionType": "GO_BACK"
         },
         {
           "style": "UNIQUE",
           "inspectionType": "GO_BACK"
         }
       ]
     }
   ]
}

const resp = await fetch(<baseURL>/totalTime, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
        "Content-Type": "application/json",
    },
})

// on success, resp.status === 200
```

## How to receive data
The data is returned as JSON and includes a single field: `totalTime`

The `totalTime` field is an integer indicating the estimated time in minutes.

In the example call above, the `totalTime` field holds 109.

### Example of receiving data
```
// resp holds response from microservice
respData = await resp.json()
console.log("total estimated time: ", respData.totalTime)

// console output: total estimated time: 109
```

## UML Diagram
<img width="483" alt="image" src="https://user-images.githubusercontent.com/64614884/218633376-87b531c7-1636-4805-a4de-1a36aabd253d.png">

