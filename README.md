# keywords

## Instructions
For this problem I would like you to recreate, in a way, the ["6 degrees of Kevin Bacon"](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) but for these keyword groups contained in the .gz xml file in this repo.
Each entry in the xml file looks like this:
```xml
<Item>
    <Keyword>customer service</Keyword>
</Item>
```
From these keyword strings you should map out each terms 1, 2, and 3 degree relations.
<br/>For example if this were our entire dataset:<br/>
`customer service`<br/>
`customer success service`<br/>
`service manager`<br/>
`success resources`<br/>
`desk manager`<br/>
For the term "customer" its 1 degree relation would be a map from term to count where customer appears in the same string as the term:<br/>
**{ 'service': 2, 'success': 1 }**<br/>
Since service appears twice in the same keyword string as customer its count is 2, while success only appears once so its count is 1.<br/>
The 2 degree relation would contain all of the terms that are 1 degree with relations with any terms in customers' 1 degree (and that aren't the term itself or contained in 1 degree):<br/>
**{ 'manager': 1, 'resources': 1 }**<br/>
And the 3 degree follows the same pattern where any term in the 2 degree's 1 degree (and is not the term itself or contained in 1 degree or 2 degree) is added:<br/>
**{ 'desk': 1 }**<br/>

<br/>*You'll notice that these maps should be in descending order with the term with the highest count first*<br/>
I would expect the output csv/xlsx/xml file to look something like this (numbers and terms are made up):
Term | 1 Degree | 2 Degree | 3 Degree
--- | --- | --- | ---
customer | { 'service': 9, 'success': 2, 'desk': 1 } | { 'sales': 45, 'management': 21 } | { 'engineering': 2 }
pet | { 'care': 23, 'hotel': 5 } | { 'grooming': 34, 'science': 10 } | { 'sales': 76, 'reminder': 6 }



