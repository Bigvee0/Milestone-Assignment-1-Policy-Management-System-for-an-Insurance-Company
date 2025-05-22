{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7500512d-9168-439d-8ff9-9c34a7e696e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import uuid\n",
    "from datetime import datetime, timedelta\n",
    "\n",
    "class Payment:\n",
    "    def __init__(self, amount, policyholder_id, product_id):\n",
    "        self.id = str(uuid.uuid4())\n",
    "        self.amount = amount\n",
    "        self.policyholder_id = policyholder_id\n",
    "        self.product_id = product_id\n",
    "        self.date = datetime.now()\n",
    "        self.status = \"completed\"\n",
    "        self.due_date = self.date + timedelta(days=30)\n",
    "        self.penalty = 0\n",
    "\n",
    "    def process_payment(self):\n",
    "        \"\"\"Process a payment.\"\"\"\n",
    "        if self.status == \"completed\":\n",
    "            return f\"Payment of {self.amount} already processed.\"\n",
    "        self.status = \"completed\"\n",
    "        self.date = datetime.now()\n",
    "        self.penalty = 0\n",
    "        return f\"Payment of {self.amount} processed successfully.\"\n",
    "\n",
    "    def send_reminder(self):\n",
    "        \"\"\"Send a payment reminder if due date is approaching.\"\"\"\n",
    "        current_date = datetime.now()\n",
    "        if current_date >= self.due_date - timedelta(days=3) and self.status != \"completed\":\n",
    "            return f\"Reminder: Payment of {self.amount} for policyholder {self.policyholder_id} is due on {self.due_date.strftime('%Y-%m-%d')}.\"\n",
    "        return \"No reminder needed.\"\n",
    "\n",
    "    def apply_penalty(self, penalty_amount):\n",
    "        \"\"\"Apply a penalty for late payment.\"\"\"\n",
    "        if self.status == \"completed\":\n",
    "            return \"Payment already completed, no penalty applied.\"\n",
    "        if datetime.now() > self.due_date:\n",
    "            self.penalty += penalty_amount\n",
    "            return f\"Penalty of {penalty_amount} applied. Total penalty: {self.penalty}.\"\n",
    "        return \"Payment not overdue, no penalty applied.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1037ccd0-6fab-41b0-8f9f-60d93e8b7cd9",
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
