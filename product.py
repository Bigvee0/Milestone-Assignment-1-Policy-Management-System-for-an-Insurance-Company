{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7177d678-8f10-4298-b77a-132957e86f39",
   "metadata": {},
   "outputs": [],
   "source": [
    "import uuid\n",
    "from datetime import datetime\n",
    "\n",
    "class Product:\n",
    "    def __init__(self, name, premium, coverage):\n",
    "        self.id = str(uuid.uuid4())\n",
    "        self.name = name\n",
    "        self.premium = premium\n",
    "        self.coverage = coverage\n",
    "        self.status = \"active\"\n",
    "        self.created_at = datetime.now()\n",
    "        self.suspended_at = None\n",
    "\n",
    "    def update(self, name=None, premium=None, coverage=None):\n",
    "        \"\"\"Update product details.\"\"\"\n",
    "        if name:\n",
    "            self.name = name\n",
    "        if premium:\n",
    "            self.premium = premium\n",
    "        if coverage:\n",
    "            self.coverage = coverage\n",
    "        return f\"Product {self.name} updated successfully.\"\n",
    "\n",
    "    def suspend(self):\n",
    "        \"\"\"Suspend a product.\"\"\"\n",
    "        if self.status == \"suspended\":\n",
    "            return f\"Product {self.name} is already suspended.\"\n",
    "        self.status = \"suspended\"\n",
    "        self.suspended_at = datetime.now()\n",
    "        return f\"Product {self.name} suspended successfully.\"\n",
    "\n",
    "    def remove(self):\n",
    "        \"\"\"Remove (suspend) a product.\"\"\"\n",
    "        return self.suspend()\n",
    "\n",
    "    def get_details(self):\n",
    "        \"\"\"Return product details.\"\"\"\n",
    "        return {\n",
    "            \"ID\": self.id,\n",
    "            \"Name\": self.name,\n",
    "            \"Premium\": self.premium,\n",
    "            \"Coverage\": self.coverage,\n",
    "            \"Status\": self.status,\n",
    "            \"Created At\": self.created_at.strftime(\"%Y-%m-%d %H:%M:%S\"),\n",
    "            \"Suspended At\": self.suspended_at.strftime(\"%Y-%m-%d %H:%M:%S\") if self.suspended_at else \"N/A\"\n",
    "        }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "947685ad-a3c8-4307-8c2a-96267754686d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
