function book(consultants, hour, duration, criteria){
    let bestConsultant = {};
    for (const consultant of consultants) {
        let available = true;
        if (!consultant.hasOwnProperty("bookings")){
            consultant["bookings"] = [];
        }
        for (const booking of (consultant.bookings)) {
            if (hour < booking.hour + booking.duration && hour + duration > booking.hour) {
                available = false;
                break;
            }
        }
        if (available) {
            if (criteria === "price") {
                if (Object.keys(bestConsultant).length === 0 || consultant.price < bestConsultant.price) {
                    bestConsultant = consultant;
                }
            } else if (criteria === "rate") {
                if (Object.keys(bestConsultant).length === 0 || consultant.rate > bestConsultant.rate) {
                    bestConsultant = consultant;
                }
            }
        }
    }
    if (bestConsultant.name){
        console.log(bestConsultant.name);
        bestConsultant.bookings = [...(bestConsultant.bookings || []), { hour, duration }];
    } else {
        console.log("No Service");
    }
}

const consultants = [
    { name: "John", rate: 4.5, price: 1000 },
    { name: "Bob", rate: 3, price: 1200 },
    { name: "Jenny", rate: 3.8, price: 800 }
];

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John