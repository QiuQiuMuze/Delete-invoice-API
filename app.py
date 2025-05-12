from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)

# 模拟发票数据库（字典）
invoices = {
    "123": "Invoice A",
    "456": "Invoice B",
    "789": "Invoice C"
}

@app.route('/deleteInvoice', methods=['DELETE'])
def delete_invoice():
    data = request.get_json()
    invoice_id = data.get("invoiceId")

    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "invoiceId": invoice_id,
    }

    if invoice_id in invoices:
        del invoices[invoice_id]
        log_entry["status"] = "success"
        message = f"Invoice {invoice_id} deleted successfully."
        success = True
    else:
        log_entry["status"] = "not_found"
        message = "Invoice not found."
        success = False

    # 写入日志文件
    with open("deletion_log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    return jsonify({
        "success": success,
        "message": message
    })

if __name__ == '__main__':
    app.run(debug=True)
