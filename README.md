# Instructions
## Please use python3 for this problem if possible
For this problem I would like you to recreate, in a way, the ["6 degrees of Kevin Bacon"](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) but for these keyword groups contained in the .gz xml file in this repo.
Each entry in the xml file looks like this:
```xml
<Item>
    <Keyword><![CDATA[customer service -0x83e3d58e80ab5964c3cdf81887e60390]]></Keyword>
</Item>
```
Your first step will be to remove the hex hash that follows the *-* along with the *-* itself and any leading or trailing whitespace. You should be left with just the keyword string and no other characters or extra whitespace.<br/><br/>
From these parsed keyword strings you should map out each unique terms 1, 2, and 3 degree relations.
<br/>For example if this were our entire dataset:<br/>
```xml
<ItemList>
    <Item>
        <Keyword><![CDATA[customer service -0x83e3d58e80ab5964c3cdf81887e60390]]></Keyword>
    </Item>
    <Item>
        <Keyword><![CDATA[customer success service -0x5f173ba9e87de36c3565787bc796e567]]></Keyword>
    </Item>
    <Item>
        <Keyword><![CDATA[service manager -0xec85a8c18dc8e59d37b97fff7f82f023]]></Keyword>
    </Item>
    <Item>
        <Keyword><![CDATA[success resources -0x1db98978e4fbd9e757a96c7f3f6c33d9]]></Keyword>
    </Item>
    <Item>
        <Keyword><![CDATA[desk manager -0xeb66e4356d472c60cc11abe1497b37da]]></Keyword>
    </Item>
</ItemList>
```
For the term **customer** its 1 degree relation would be a map from unique term to count of each term that appears in the same keyword string as **customer**:<br/>
**{ 'service': 2, 'success': 1 }**<br/>
Since service appears twice in the same keyword string as customer its count is 2, while success only appears once so its count is 1.<br/><br/>
The 2 degree relation would contain all of the terms that are 1 degree relations with any terms in customers' 1 degree (*and that aren't **customer** itself or contained in customers' 1 degree*):<br/>
**{ 'manager': 1, 'resources': 1 }**<br/><br/>
And the 3 degree follows the same pattern where any term in the 2 degree's 1 degree (*and is not the term itself or contained in 1 degree or 2 degree*) is added:<br/>
**{ 'desk': 1 }**<br/><br/>
<br/>*You'll notice that these maps should be in descending order with the term with the highest count first*<br/>
<br/><br/>Once you have calculated the 1, 2, and 3 degree relations for each term you should write that data to a csv or xlsx or xml file. Whichever you prefer.<br/>
I would expect the output csv/xlsx/xml file to look something like this (*I've only done the term **customer** for you, there would be 6 rows in this example, 1 for each unique term in the dataset*):
Term | 1 Degree | 2 Degree | 3 Degree
--- | --- | --- | ---
customer | { 'service': 2, 'success': 1 } | { 'manager': 1, 'resources': 1 } | { 'desk': 1 }



