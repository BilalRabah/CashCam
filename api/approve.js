const axios = require('axios');
module.exports = async (req, res) => {
res.setHeader('Access-Control-Allow-Origin', '*');
res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
if (req.method === 'OPTIONS') {
return res.status(200).end();
}
const paymentId = req.body.paymentId;
try {
await axios.post(
https://api.minepi.com/v2/payments/${paymentId}/approve,
{},
{
headers: {
Authorization: fqbrs4owitj1f8foektnajj40upqzmyyu5p1mgg4ghcvn67esfgkgb1sbvuiiuk1
}
}
);
res.send({ success: true });
} catch (error) {
res.status(500).send({ success: false, error: error.message });
}
};
