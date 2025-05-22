{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "10959d6a-a281-4fda-b3e0-dd300d2f73af",
   "metadata": {},
   "outputs": [],
   "source": [
    "# policyholder.py\n",
    "\n",
    "class Policyholder:\n",
    "    def __init__(self, holder_id, name, email):\n",
    "        self.holder_id = holder_id\n",
    "        self.name = name\n",
    "        self.email = email\n",
    "        self.active = True\n",
    "\n",
    "    def suspend(self):\n",
    "        self.active = False\n",
    "        print(f\"Policyholder {self.name} has been suspended.\")\n",
    "\n",
    "    def reactivate(self):\n",
    "        self.active = True\n",
    "        print(f\"Policyholder {self.name} has been reactivated.\")\n",
    "\n",
    "    def update_details(self, name=None, email=None):\n",
    "        if name:\n",
    "            self.name = name\n",
    "        if email:\n",
    "            self.email = email\n",
    "        print(f\"Policyholder {self.holder_id} details updated.\")\n",
    "\n",
    "    def __str__(self):\n",
    "        status = \"Active\" if self.active else \"Suspended\"\n",
    "        return f\"ID: {self.holder_id}, Name: {self.name}, Email: {self.email}, Status: {status}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c1400d1-a0be-4627-a9a8-221cd2136d84",
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
