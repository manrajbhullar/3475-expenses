# Working on Expenses

## Running the Flask server
- cd into directory, do `python3 -m venv venv` (on windows: `py -3 -m venv venv`)
- and then run `source venv/bin/activate` (on windows: `source venv/Scripts/activate` (The capital 'S' in Scripts matters!)
- (if first time working) run `pip3 install Flask && pip install flask_mongoengine`
- type `python main.py` in the console
- visit `http://localhost:5000` in your web browser
- try not to break anything!
- make sure mongodb compass is installed: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/

## About HTML pages
- to reduce reused code, all our html pages will "extend" the base html page `templates/layout.html`
    - this layout page has the doctype, header, and basic page layout tags already
- all pages for each section of the app are in `templates/views/` directory
    - for example, the List Expenses page is `templates/views/list_expenses.html`
