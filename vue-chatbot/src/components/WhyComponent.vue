<template>
  <section class="why_section layout_padding">
    <div class="container">
      <div class="heading_container heading_center">
        <h2>
          Why Choose <span>Us</span>
        </h2>
      </div>
      <div class="why_container">
        <div class="box">
          <div class="img-box">
            <img src="@/assets/images/w1.png" alt="Expert Management">
          </div>
          <div class="detail-box">
            <h5>
              Expert Management
            </h5>
            <p>
              Our team of seasoned professionals brings extensive industry experience and expert management to your investments. We stay ahead of market trends to provide you with the best opportunities, ensuring your portfolio is in capable hands.
            </p>
          </div>
        </div>
        <div class="box">
          <div class="img-box">
            <img src="@/assets/images/w2.png" alt="Secure Investment">
          </div>
          <div class="detail-box">
            <h5>
              Secure Investment
            </h5>
            <p>
              We prioritize the security of your investments with cutting-edge technology and robust risk management strategies. Our transparent and ethical approach ensures that your assets are always protected.
            </p>
          </div>
        </div>
        <div class="box">
          <div class="img-box">
            <img src="@/assets/images/w3.png" alt="Instant Trading">
          </div>
          <div class="detail-box">
            <h5>
              Instant Trading
            </h5>
            <p>
              Our platform allows you to execute trades instantly, giving you the edge in a fast-paced market. Enjoy seamless and efficient trading experiences with real-time data and analytics at your fingertips.
            </p>
          </div>
        </div>
        <div class="box">
          <div class="img-box">
            <img src="@/assets/images/w4.png" alt="Happy Customers">
          </div>
          <div class="detail-box">
            <h5>
              Happy Customers
            </h5>
            <p>
              Our commitment to exceptional customer service has earned us the trust and satisfaction of our clients. We go above and beyond to ensure your experience with us is positive and rewarding.
            </p>
          </div>
        </div>
      </div>
      <div class="btn-box">
        <router-link class="nav-link" to="/why">Read More</router-link>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'WhyComponent'
}
</script>

<style scoped>
@import '../assets/css/bootstrap.css';
@import '../assets/css/font-awesome.min.css';
@import '../assets/css/style.css';
@import '../assets/css/responsive.css';
</style>
