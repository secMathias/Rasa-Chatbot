<template>
  <!-- service section -->
  <section class="service_section layout_padding">
    <div class="service_container">
      <div class="container">
        <div class="heading_container heading_center">
          <h2>
            Our <span>Services</span>
          </h2>
          <p>
            We offer a range of services designed to meet your financial needs with excellence and innovation.
          </p>
        </div>
        <div class="row">
          <div class="col-md-4">
            <div class="box">
              <div class="img-box">
                <img src="@/assets/images/s1.png" alt="Currency Wallet">
              </div>
              <div class="detail-box">
                <h5>
                  Currency Wallet
                </h5>
                <p>
                  Securely manage your cryptocurrencies with our state-of-the-art currency wallet. Enjoy the convenience of easy access and the peace of mind that your assets are protected with advanced security features.
                </p>
                <router-link class="nav-link" to="/service">Read More</router-link>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="box">
              <div class="img-box">
                <img src="@/assets/images/s2.png" alt="Security Storage">
              </div>
              <div class="detail-box">
                <h5>
                  Security Storage
                </h5>
                <p>
                  Keep your digital assets safe with our top-tier security storage solutions. We provide robust protection against unauthorized access, ensuring your investments are always secure.
                </p>
                <router-link class="nav-link" to="/service">Read More</router-link>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="box">
              <div class="img-box">
                <img src="@/assets/images/s3.png" alt="Expert Support">
              </div>
              <div class="detail-box">
                <h5>
                  Expert Support
                </h5>
                <p>
                  Our team of experts is available around the clock to offer you comprehensive support. Whether you need help with transactions or advice on market trends, we are here to assist you every step of the way.
                </p>
                <router-link class="nav-link" to="/service">Read More</router-link>
              </div>
            </div>
          </div>
        </div>
        <div class="btn-box">
          <router-link class="nav-link" to="/service">View All</router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ServiceComponent'
}
</script>

<style scoped>
@import '../assets/css/bootstrap.css';
@import '../assets/css/font-awesome.min.css';
@import '../assets/css/style.css';
@import '../assets/css/responsive.css';
</style>
