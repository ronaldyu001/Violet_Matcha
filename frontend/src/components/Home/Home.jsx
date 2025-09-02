import React, { useState } from 'react';
// import image0 from '../../assets/images/homepage_header/Matcha-Featured-Tea_600x600.webp'
import image0 from '../../assets/images/homepage_header/matcha-tea-frame-background-in-flat-design-vector.jpg'
import image1 from '../../assets/images/matchas/ChiginoShiroMatchaMarukyuKoyamaen1_3000x.webp';
import image2 from '../../assets/images/matchas/EijuMatchaMarukyuKoyamaen1_3000x.webp';
import image3 from '../../assets/images/matchas/IsuzuMatchaMarukyuKoyamaen1_3000x.webp';
import image4 from '../../assets/images/matchas/KinrinMatchaMarukyuKoyamaen1_3000x.webp';
import image5 from '../../assets/images/matchas/MarukyuKoyamaenWakoMatcha1_3000x.webp';
import image6 from '../../assets/images/matchas/YugenMatchaMarukyuKoyamaen1_3000x.webp';
import image7 from '../../assets/images/matchas/aoarashi-matcha-by-marukyu-koyamaen-40-gram-or-100-gram-tins-890738_3000x.webp';
import image8 from '../../assets/images/matchas/unkaku-uji-matcha-by-marukyu-koyamaen-189269_3000x.webp'
import image9 from '../../assets/images/matchas/MarukyuKoyamaenChoanMatchasm_c956ed1f-f8c4-4fc3-9c8a-52ef6d6d09b0_3000x.webp'


const products = [
  { id: 1, name: 'Chigi no Shiro Matcha by Marukyu Koyamaen', image: image1 },
  { id: 2, name: 'Eiju Matcha by Marukyu Koyamaen', image: image2 },
  { id: 3, name: 'Isuzu Matcha by Marukyu Koyamaen', image: image3},
  { id: 4, name: 'Kinrin Matcha by Marukyu Koyamaen', image: image4},
  { id: 5, name: 'Wako Matcha by Marukyu Koyamaen', image: image5},
  { id: 6, name: 'Yugen Matcha by Marukyu Koyamaen', image: image6},
  { id: 7, name: 'Aoarashi Matcha by Marukyu Koyamaen', image: image7},
  { id: 8, name: 'Unkaku Uji Matcha by Marukyu Koyamaen', image: image8},
  { id: 9, name: 'Choan Matcha by Marukyu Koyamaen', image: image9},
];

export default function Home() {
  const [cart, setCart] = useState({});
  const [isLive, setIsLive] = useState(false);


  const addToCart = (productId) => {
    setCart((prevCart) => ({
      ...prevCart,
      [productId]: (prevCart[productId] || 0) + 1,
    }));
  };


  const cartItems = Object.entries(cart).map(([id, qty]) => {
    const product = products.find((p) => p.id === parseInt(id));
    return {
      ...product,
      quantity: qty,
    };
  });


  const removeFromCart = (productId) => {
    setCart((prevCart) => {
      const updatedCart = { ...prevCart };
      if (updatedCart[productId] > 1) {
        updatedCart[productId] -= 1;
      } else {
        delete updatedCart[productId];
      }
      return updatedCart;
    });
  };


  const handleCancel = () => {
    console.log("Canceling service.")
    setIsLive(false)
  }
  

  const handleOrder = async () => {
    // get orders
    console.log("Creating order list.");
    const order_list = [];
    cartItems.forEach(item => { order_list.push({ name: item.name, quantity: item.quantity })});
    console.log(order_list);

    // create payload
    console.log("Creating order payload.");
    const payload = {
      orders: order_list,
      active: true
    };
    console.log(payload);

    // send payload
    try {
      const response = await fetch("http://localhost:8000/api/order_matcha", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });

      const data = await response.json();
      console.log("Response from backend:", data);
    } catch (error) {
      console.error("Error sending order:", error);
    } finally{
      setIsLive(false)
    }
  };
  

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', backgroundColor: '#FFF', margin: 0, padding: 0 }}>

      {/* Header Image */}
      <div style={{ width: '100vw', height: '30vh', position: 'relative' }}>
        <img
          src={image0}
          alt="Homepage header"
          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        />
        <h1
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            fontSize: '4rem',
            color: 'white',
            textShadow: '2px 2px 4px rgba(0,0,0,0.5)',
            margin: 0,
            fontFamily: 'serif',
            letterSpacing: '2px',
            color: '#333'
          }}
        >
          Matcha.
        </h1>
      </div>

      {/* Main content: scrollable matchas + fixed cart */}
      <div style={{ display: 'flex', flex: 1, overflow: 'hidden' }}>

        {/* Scrollable matcha list */}
        <div style={{ flex: 3, overflowY: 'auto', padding: '2rem' }}>
          <div  style={{ display: 'grid', gap: '2rem', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))' }}>
            
            {products.map((product) => (
              <div  key={product.id}
                    style={{ padding: '1rem', textAlign: 'center', backgroundColor: "#FFF", height: '40vh', boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)' }}>
                <img  src={product.image}
                      alt={product.name}
                      style={{ width: '50%', height: '50%', objectFit: 'cover' }}/>
                <h3 style={{ textAlign: 'left',fontSize: '15px', fontWeight: 100, margin: '0.5rem 0', color: 'black', borderLeft: '1px solid #ccc', padding: '5%' }}>
                  {product.name}
                </h3>
                <button
                  onClick={() => addToCart(product.id)}
                  style={{
                    marginTop: '15%',
                    padding: '0.5rem 1rem',
                    cursor: 'pointer',
                    border: 'none',
                    backgroundColor: '#222',
                    color: '#fff',
                    borderRadius: '999px',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.5rem',
                    fontSize: '0.9rem',
                    fontWeight: 500,
                    transition: 'background-color 0.2s ease',
                    justifySelf: 'center'
                  }}
                  onMouseOver={e => e.currentTarget.style.backgroundColor = '#444'}
                  onMouseOut={e => e.currentTarget.style.backgroundColor = '#222'}
                >
                  🛒 Add to Cart
                </button>
              </div>
            ))}
          </div>
        </div>

        {/* Cart */}
       <div
          style={{
            flex: 1,
            display: 'flex',
            flexDirection: 'column',
            borderLeft: '1px solid #ccc',
            backgroundColor: '#f7f7f7',
            height: '100%',
          }}
        >
          {/* Scrollable cart items */}
          <div style={{ flex: 1, overflowY: 'auto', padding: '1rem' }}>
            <h2>Cart</h2>
            {cartItems.length === 0 ? (
              <p>Your cart is empty</p>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                {cartItems.map((item) => (
                  <div
                    key={item.id}
                    style={{
                      backgroundColor: '#fff',
                      padding: '0.75rem 1rem',
                      borderRadius: '8px',
                      boxShadow: '0 1px 4px rgba(0, 0, 0, 0.05)',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                    }}
                  >
                    <span style={{ fontSize: '0.85rem', width: '65%', fontWeight: 500 }}>{item.name}</span>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                      <span style={{ fontSize: '0.85rem', width: '20px', color: '#666' }}>× {item.quantity}</span>
                      <button
                        onClick={() => removeFromCart(item.id)}
                        style={{
                          background: 'transparent',
                          border: 'none',
                          color: '#888',
                          fontSize: '1rem',
                          cursor: 'pointer',
                        }}
                        title="Remove"
                      >
                        🗑
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Fixed footer toggle */}
          <div
            style={{
              padding: '1rem',
              borderTop: '1px solid #ddd',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              rowGap: '0.5rem',
              backgroundColor: '#f7f7f7',
            }}
          >
            <div
              onClick={() => {
                setIsLive(prev => {
                  const next = !prev;
                  if (next) handleOrder(); 
                  else handleCancel();
                  return next;
                });
              }}
              style={{
                width: '50px',
                height: '25px',
                borderRadius: '999px',
                backgroundColor: isLive ? '#4ade80' : '#ccc',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                padding: '2px',
                transition: 'background-color 0.3s ease',
              }}
            >
              <div
                style={{
                  height: '21px',
                  width: '21px',
                  borderRadius: '50%',
                  backgroundColor: '#fff',
                  transform: isLive ? 'translateX(25px)' : 'translateX(0)',
                  transition: 'transform 0.3s ease',
                }}
              />
            </div>
            {isLive && (
              <span style={{ fontSize: '0.85rem', color: '#555' }}>
                Waiting for items to go live...
              </span>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}