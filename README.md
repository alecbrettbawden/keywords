# keywords

## Instructions
For this problem I would like you to recreate, in a way, the ["6 degrees of Kevin Bacon"](https://en.wikipedia.org/wiki/Six_degrees_of_separation) but for these keyword groups contained in the .gz xml file in this repo.
Each entry in the xml file looks like this:
```xml
<Item>
    <Keyword>test string</Keyword>
</Item>
```
I would expect the output csv/xlsx/xml file to look something like this:
Term | 1 Degree | 2 Degree | 3 Degree
--- | --- | --- | ---
customer | {  } | {  } | {  }
pet | { 'care': 23, 'hotel': 5 } | { 'grooming': 34, 'science': 10 } | { 'sales': 76, 'reminder': 6 }



