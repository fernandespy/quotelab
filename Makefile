run:
	uvicorn quotelab.main:app --reload

test:
	python -m pytest