CREATE TABLE Register (
    cid int PRIMARY KEY AUTO_INCREMENT,
    firstname varchar(255),
    lastName varchar(255),
    phone bigint,
    email varchar(255),
    pwd varchar(255)
);

CREATE TABLE Booking (
    bid int PRIMARY KEY AUTO_INCREMENT,
    cid int,
    FOREIGN KEY (cid) REFERENCES Register(cid),
    date date,
    time time,
    people int,
    pickupLocation varchar(255),
    dropoffLocation varchar(255)
);

CREATE TABLE Drivers (
    did int PRIMARY KEY AUTO_INCREMENT,
    name varchar(255),
    phone bigint,
    license varchar(255),
    car varchar(255),
    address varchar(255),
    joinDate date,
    status varchar(255),
    salary int
);

CREATE TABLE Vehicles (
    vid int PRIMARY KEY AUTO_INCREMENT,
    did int,
    FOREIGN KEY (did) REFERENCES Drivers(did),
    licensePlate varchar(255) PRIMARY KEY,
    name varchar(255),
    model varchar(255),
    seats int,
    status varchar(255)
);

CREATE TABLE BookingDetails (
    bid int,
    FOREIGN KEY (bid) REFERENCES Booking(bid),
    vid int,
    FOREIGN KEY (vid) REFERENCES Vehicles(vid),
    did int,
    FOREIGN KEY (did) REFERENCES Drivers(did),
    PRIMARY KEY (bid, vid, did)
    pickupTime time,
    FOREIGN KEY (pickupLocation) REFERENCES Booking(pickupLocation),
    dropoffTime time,
    FOREIGN KEY (dropoffLocation) REFERENCES Booking(dropoffLocation),
    price int,
    cancel varchar(255)
);

