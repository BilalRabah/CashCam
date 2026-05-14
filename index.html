<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CashCam - Pi Network Integration</title>
    <!-- استدعاء أحدث نسخة من الـ SDK -->
    <script src="https://sdk.minepi.com/pi-sdk.js"></script>
</head>
<body>
    <h1>CashCam App is Running!</h1>
    <p>Status: Integration in Progress</p>
    
    <button id="pay-button" style="padding: 15px; background: #673ab7; color: white; border: none; border-radius: 8px;">
        Pay 0.5 Pi (Testnet)
    </button>

    <script>
        // تهيئة الـ SDK
        const Pi = window.Pi;
        Pi.init({ version: "2.0", sandbox: true }); // اجعل sandbox: false عند الانتقال للماينيت

        document.getElementById('pay-button').onclick = function() {
            try {
                const payment = Pi.createPayment({
                    amount: 0.5,
                    memo: "Testing CashCam Premium Features",
                    metadata: { productId: "premium_001" },
                }, {
                    onReadyForServerApproval: function(paymentId) {
                        console.log("Payment ID for server approval:", paymentId);
                        // هنا يتم إرسال المعرف للسيرفر إذا كان لديك سيرفر خلفي
                    },
                    onReadyForServerCompletion: function(paymentId, txid) {
                        console.log("Payment ready for completion. TXID:", txid);
                    },
                    onCancel: function(paymentId) {
                        console.log("Payment cancelled.");
                    },
                    onError: function(error, payment) {
                        console.error("Payment error occurred:", error);
                        alert("Error: " + error.message);
                    },
                });
            } catch (err) {
                console.error("Initialization error:", err);
            }
        };
    </script>
</body>
</html>
