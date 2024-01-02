V_PY		= py

training:
		$(V_PY) linear_regression.py
data:
		$(V_PY) linear_regression.py -d
line:
		$(V_PY) linear_regression.py -l
precise:
		$(V_PY) linear_regression.py -p
predict:
		$(V_PY) mileage.py
clean:
		$(V_PY) linear_regression.py -c